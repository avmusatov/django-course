import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutusComponent } from './aboutus/aboutus.component';
import { DonationComponent } from './donation/donation.component';

import { PetComponent } from './pet/pet.component'

const routes: Routes = [
  { path: 'pets', component: PetComponent },
  { path: '', redirectTo: '/pets', pathMatch: 'full' },
  { path: 'donation', component: DonationComponent },
  { path: 'aboutus', component: AboutusComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
