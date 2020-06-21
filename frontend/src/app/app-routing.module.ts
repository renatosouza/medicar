import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ListaConsultasComponent } from './lista-consultas/lista-consultas.component';
import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';
import { RegistroComponent } from './registro/registro.component';
import { LoginComponent } from './login/login.component';

import { LoggedInGuard } from './logged-in.guard';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: ListaConsultasComponent, canActivate: [LoggedInGuard] },
  { path: 'nova', component: NovaConsultaComponent, canActivate: [LoggedInGuard] },
  { path: 'registro', component: RegistroComponent },

  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [LoggedInGuard]
})
export class AppRoutingModule { }
