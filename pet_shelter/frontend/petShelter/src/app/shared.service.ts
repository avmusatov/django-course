import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Pet } from './shared/Pet';
import { Donation } from './shared/Donation';
import { Leader } from './shared/Leader';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000/api";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/"

  constructor(private http: HttpClient) { }

  getPetList(): Observable<Pet[]> {
    return this.http.get<any[]>(this.APIUrl + '/pets/');
  }

  addPet(value: Pet) {
    return this.http.post(this.APIUrl + '/pets/', value);
  }

  updatePet(id: number, value: Pet) {
    return this.http.put(this.APIUrl + `/pets/${id}`, value);
  }

  deletePet(id: number) {
    return this.http.delete(this.APIUrl + `/pets/${id}`);
  }

  getDonationList(): Observable<Donation[]> {
    return this.http.get<Donation[]>(this.APIUrl + '/donations/');
  }

  addDonation(donation: Donation) {
    return this.http.post(this.APIUrl + '/donations/', donation);
  }

  getLeadersList(): Observable<Leader[]> {
    return this.http.get<Leader[]>(this.APIUrl + '/leaders/');
  }
}
