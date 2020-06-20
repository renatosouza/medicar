import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-lista-consultas',
  templateUrl: './lista-consultas.component.html',
  styleUrls: ['./lista-consultas.component.css']
})
export class ListaConsultasComponent implements OnInit {
  consultas = [];
  loadedConsultas: boolean;

  constructor(private apiService: ApiService) {
    this.loadedConsultas = false;
  }

  ngOnInit(): void {
    this.consultas = JSON.parse(localStorage.getItem('consultas'));

    if(this.consultas) {
      this.loadedConsultas = true
    } else {
      this.apiService.getConsultas()
        .subscribe(data => {
          this.consultas = [...data];
          localStorage.setItem('consultas', JSON.stringify(this.consultas));
          this.loadedConsultas = true;     
        });
    }
  }

  onDesmarcaConsulta(id: number): void {
    this.consultas = this.consultas.filter(consulta => consulta.id !== id);
    localStorage.setItem('consultas', JSON.stringify(this.consultas));
    this.apiService.deleteConsulta(id).subscribe();
  }

}
