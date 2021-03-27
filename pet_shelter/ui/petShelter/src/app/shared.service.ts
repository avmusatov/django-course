import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000/api";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/"

  constructor(private http: HttpClient) { }

  getPetList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/pets/');
  }

  addPet(value:any) {
    return this.http.post(this.APIUrl + '/pets/',value);
  }

  updatePet(id:number, value:any) {
    return this.http.put(this.APIUrl + `/pets/${id}`, value);
  }

  deletePet(id:number) {
    return this.http.delete(this.APIUrl + `/pets/${id}`);
  }
}
