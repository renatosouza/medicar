import { Injectable } from '@angular/core';


@Injectable()
export class AuthService {

  constructor() { 
  }

  setLogin(token: string, username: string) {
    localStorage.setItem('token', token);
    localStorage.setItem('username', username);
  }

  logout() {
    localStorage.clear();
  }

  isLoggedIn(): boolean {
    const user = localStorage.getItem('username');
    return user!==null;
  }
}