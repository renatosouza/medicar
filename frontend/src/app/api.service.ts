import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class ApiService {
  apiUrl = 'http://localhost:8000'
  loggedIn: boolean;

  constructor(private http: HttpClient) { 
  }

  login(credentials: object): Observable<object> {
    return this.http.post<object>(`${this.apiUrl}/api-token-auth/`, credentials); 
  }

  registro(data: object): Observable<object> {
    return this.http.post<object>(`${this.apiUrl}/register/`, data);
  }

  getConsultas(): Observable<object[]> {
    const token = localStorage.getItem('token');
    const header = new HttpHeaders({Authorization: `Token ${token}`});
    return this.http.get<object[]>(`${this.apiUrl}/consultas/`, {headers: header});
  }

  deleteConsulta(id: number): Observable<{}> {
    const token = localStorage.getItem('token');
    const header = new HttpHeaders({Authorization: `Token ${token}`});
    return this.http.delete(`${this.apiUrl}/consultas/${id}`, {headers: header});
  }
  // getEspecialidades(): Observable<object[]> {
  //   return this.http.get<object[]>(`${this.apiUrl}/especialidades/`, {headers: this.header});
  // }
}
