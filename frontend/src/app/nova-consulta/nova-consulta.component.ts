import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-nova-consulta',
  templateUrl: './nova-consulta.component.html',
  styleUrls: ['./nova-consulta.component.css']
})
export class NovaConsultaComponent implements OnInit {
  especialidades = [
    {
      id: 1,
      nome: 'Pediatria'
    },
    {
      id: 2,
      nome: 'Nefrologia'
    },
    {
      id: 3,
      nome: 'Cardiologia'
    },
  ];

  medicos = [
    {
      id: 1,
      nome: 'Gregory House'
    },
    {
      id: 2,
      nome: 'James Wilson'
    },
    {
      id: 3,
      nome: 'Lisa Cuddy'
    },
  ];

  datas = [
    {
      id: 1,
      nome: '20/06/2020',
      horas: ['10:00', '11:00', '12:00']
    },
    {
      id: 2,
      nome: '21/06/2020',
      horas: ['13:00', '14:00', '15:00']
    },
    {
      id: 3,
      nome: '22/06/2020',
      horas: ['16:00', '17:00', '18:00']
    },
  ];

  horas: String[];

  form: FormGroup;

  constructor(fb: FormBuilder) { 
    this.form = fb.group({
      'especialidade': [null, Validators.required],
      'medico': [null, Validators.required],
      'data': [null, Validators.required],
      'hora': [null, Validators.required]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    console.log(this.form.value);
  }

  onChangeData(): void {
    const data_selecionada = this.form.get('data').value;
    this.horas = [...data_selecionada.horas];
  }

}
