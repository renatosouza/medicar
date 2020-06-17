import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


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

  constructor(fb: FormBuilder) { 
    this.form = fb.group({
      'username': [null, Validators.required],
      'email': [null, Validators.required],
      'password': [null, Validators.required],
      'password2': [null, Validators.required]
    }, { validator: confirmaSenhaValidation });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    console.log(this.form.value);
  }

}
