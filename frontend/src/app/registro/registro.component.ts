import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

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

  constructor(fb: FormBuilder, private apiService: ApiService) { 
    this.form = fb.group({
      'username': [null, Validators.required],
      'email': [null, Validators.required],
      'password': [null, Validators.required],
      'password2': [null, Validators.required]
    }, { validator: confirmaSenhaValidation });
  }

  ngOnInit(): void {
  }

  registro(): void {
    const dados = {
      'username': this.form.get('username').value,
      'email': this.form.get('email').value,
      'password': this.form.get('password').value
    }
    this.apiService.registro(dados)
      .subscribe(
        data => {
          console.log(data)
          //fazer login automatico ou redirecionar pra página de login?
          //se redirecionar, necessário mensagem de sucesso de cadastro
        }, errors => {
          this.form.reset()
          //setar erro de Usuário já existente
          //mensagem de erro
          //erro caso email em formato errado?
        });
  }

}
