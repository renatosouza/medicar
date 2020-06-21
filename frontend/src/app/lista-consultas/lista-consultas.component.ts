import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';


@Component({
  selector: 'app-lista-consultas',
  templateUrl: './lista-consultas.component.html',
  styleUrls: ['./lista-consultas.component.css']
})
export class ListaConsultasComponent implements OnInit {
  consultas = [];
  loadedConsultas: boolean;

  constructor(private apiService: ApiService, private router: Router) {
    this.loadedConsultas = false;
  }

  ngOnInit(): void {
    this.apiService.getConsultas()
      .subscribe(data => {
        this.consultas = [...data];
        this.loadedConsultas = true;
      })
  }

  onDesmarcaConsulta(id: number): void {
    this.consultas = this.consultas.filter(consulta => consulta.id !== id);
    this.apiService.deleteConsulta(id).subscribe();
  }

}
