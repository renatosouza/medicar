import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class ApiService {
  apiUrl = 'http://localhost:8000'
  header: HttpHeaders;

  constructor(private http: HttpClient) { 
  }

  setTokenOnHeader(token: string) {
    this.header = new HttpHeaders({Authorization: `Token ${token}`});
  }

  login(credentials: object): Observable<object> {
    return this.http.post<object>(`${this.apiUrl}/api-token-auth/`, credentials); 
  }

  // getEspecialidades(): Observable<object[]> {
  //   return this.http.get<object[]>(`${this.apiUrl}/especialidades/`, {headers: this.header});
  // }
}
