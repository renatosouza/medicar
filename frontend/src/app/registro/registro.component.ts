import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';


function confirmaSenhaValidation(group: FormGroup): {[s: string]: boolean} {
  if((!group) || (!group.get('password')) || (!group.get('password2'))) {
    return null;
  }
  let password = group.get('password').value;
  let password2 = group.get('password2').value;

  return password === password2 ? null : { notSame: true } 
}

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  form: FormGroup;

  constructor(fb: FormBuilder, private apiService: ApiService, private router: Router) { 
    this.form = fb.group({
      'username': [null, Validators.required],
      'email': [null, Validators.required],
      'password': [null, Validators.required],
      'password2': [null, Validators.required]
    }, { validator: confirmaSenhaValidation });
  }

  ngOnInit(): void {
    localStorage.clear();
  }

  registro(): void {
    const dados = {
      username: this.form.get('username').value,
      email: this.form.get('email').value,
      password: this.form.get('password').value
    }
    this.apiService.registro(dados)
      .subscribe(
        data => {
          const { email, ...credenciais } = dados;
          this.apiService.login(credenciais)
            .subscribe(loginData => {
              localStorage.setItem('token', loginData['token']);
              localStorage.setItem('username', credenciais.username);
              this.router.navigate(['home']);
            })
        }, errors => {
          this.form.reset();
          this.form.setErrors({'Existente': true});
        });
  }

}
