import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';
import { Pet } from '../shared/Pet';

@Component({
  selector: 'app-pet',
  templateUrl: './pet.component.html',
  styleUrls: ['./pet.component.css']
})
export class PetComponent implements OnInit {

  constructor(private sharedService: SharedService) { }

  pets: Pet[];

  ngOnInit(): void {
    this.sharedService.getPetList().subscribe(data => this.pets = data);
  }
}
