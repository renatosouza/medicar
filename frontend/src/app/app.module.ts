import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { ListaConsultasComponent } from './lista-consultas/lista-consultas.component';
import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';

import { ApiService } from './api.service';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: ListaConsultasComponent },
  { path: 'nova', component: NovaConsultaComponent },
  { path: 'registro', component: RegistroComponent },

  { path: 'login', component: LoginComponent },
]

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ListaConsultasComponent,
    NovaConsultaComponent,
    LoginComponent,
    RegistroComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
