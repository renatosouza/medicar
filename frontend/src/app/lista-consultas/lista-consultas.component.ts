import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lista-consultas',
  templateUrl: './lista-consultas.component.html',
  styleUrls: ['./lista-consultas.component.css']
})
export class ListaConsultasComponent implements OnInit {
  consultas = [
    {
      "id": 1,
      "dia": "2020-02-05",
      "horario": "12:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
      }
    },
    {
      "id": 2,
      "dia": "2020-03-01",
      "horario": "09:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
      }
    },
    {
      "id": 3,
      "dia": "2020-06-11",
      "horario": "10:00",
      "data_agendamento": "2020-06-10T18:35:53.255636-03:00",
      "medico": {
        "id": 3,
        "crm": 464,
        "nome": "Lisa Cuddy",
        "especialidade": {
          "id": 4,
          "nome": "Cardiologia"
        },
        "telefone": "",
        "email": ""
      }
    },
    {
      "id": 4,
      "dia": "2020-06-11",
      "horario": "09:00",
      "data_agendamento": "2020-06-10T18:43:27.154291-03:00",
      "medico": {
        "id": 2,
        "crm": 4654,
        "nome": "James Wilson",
        "especialidade": {
          "id": 5,
          "nome": "Oncologia"
        },
        "telefone": "",
        "email": ""
      }
    }
  ]

  constructor() { }

  ngOnInit(): void {
  }

  onDesmarcaConsulta(id: number): void {
    this.consultas = this.consultas.filter(consulta => consulta.id !== id);
  }

}
