import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(fb: FormBuilder, private apiService: ApiService, private router: Router) { 
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  login(): void {
    this.apiService.login(this.form.value)
      .subscribe(data => {
        this.apiService.setTokenOnHeader(data['token']);
        this.router.navigate(['home']);
      }, error => {
        this.form.reset();
        this.form.setErrors({'Inexistente':true});
      });
  }

}
