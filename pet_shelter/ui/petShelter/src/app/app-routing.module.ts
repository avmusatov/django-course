import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PetComponent } from './pet/pet.component'

const routes: Routes = [
  { path: 'pets', component: PetComponent },
  { path: '', redirectTo: '/pets', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
