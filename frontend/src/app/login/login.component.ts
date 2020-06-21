import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(fb: FormBuilder, private apiService: ApiService, private router: Router, private authService: AuthService) { 
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
  }

  ngOnInit(): void {
    if (this.authService.isLoggedIn()) {
      this.router.navigate(['home']);
    }
  }

  login(): void {
    this.apiService.login(this.form.value)
      .subscribe(data => {
        this.authService.setLogin(data['token'], this.form.get('username').value);
        this.router.navigate(['home']);
      }, error => {
        this.form.reset();
        this.form.setErrors({'Inexistente': true});
      });
  }

}
