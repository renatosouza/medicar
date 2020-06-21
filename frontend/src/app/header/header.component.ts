import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  usuario: string;

  constructor(private router: Router, private authService: AuthService) { 
    this.usuario = localStorage.getItem('username');
  }

  ngOnInit(): void {
  }

  onLogout() {
    this.authService.logout();
    this.router.navigate(['login']);
  }

}
