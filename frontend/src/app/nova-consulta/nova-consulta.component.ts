import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';


@Component({
  selector: 'app-nova-consulta',
  templateUrl: './nova-consulta.component.html',
  styleUrls: ['./nova-consulta.component.css']
})
export class NovaConsultaComponent implements OnInit {
  especialidades = [];
  especialidadeSelecionada: object;
  medicos = [];
  medicoSelecionado: object;
  agendas = [];
  agendaSelecionada: object;
  horarios = [];
  horarioSelecionado: object;
  form: FormGroup;

  constructor(fb: FormBuilder, private apiService: ApiService, private router: Router) { 
    this.form = fb.group({
      'especialidade': [null, Validators.required],
      'medico': [null, Validators.required],
      'data': [null, Validators.required],
      'hora': [null, Validators.required]
    });
  }

  ngOnInit(): void {
    this.apiService.getEspecialidades()
      .subscribe(data => this.especialidades = [...data]);
  }

  onChangeEspecialidade(especialidadeId: string) {
    const id = parseInt(especialidadeId);

    this.apiService.getMedicosPorEspecialidade(id)
      .subscribe(data => this.medicos = [...data]);

    this.agendas = [];
    this.horarios = [];
  }

  onChangeMedico(medicoId: string) {
    const id = parseInt(medicoId);

    this.apiService.getAgendasPorMedico(id)
      .subscribe(data => this.agendas = [...data]);

    this.horarios = [];
  }

  onChangeAgenda(agendaId: string) {
    const id = parseInt(agendaId);
    
    this.agendaSelecionada = this.agendas
      .find(medico => medico.id === id);

    this.horarios = [...this.agendaSelecionada['horarios']];
  }

  criaConsulta(): void {
    const dados = {
      agenda_id: parseInt(this.form.get('data').value),
      horario: this.form.get('hora').value
    }
    this.apiService.createConsulta(dados)
      .subscribe(data => {
        this.router.navigate(['home']);
      }, errors => {
        // this.form.reset();
        this.form.setErrors({'Indisponivel': true});
      });
  }
}
