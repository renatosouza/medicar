import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { ApiService } from '../api.service';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(fb: FormBuilder, private apiService: ApiService, private httpClient: HttpClient) { 
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.apiService.login(this.form.value)
      .subscribe(data => {
        this.apiService.setTokenOnHeader(data['token']);
      }, error => {
        this.form.reset();
        this.form.setErrors({'Inexistente':true});
      });
  }

}
