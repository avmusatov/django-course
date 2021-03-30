import { Component, OnInit, Renderer2} from '@angular/core';
import { SharedService } from '../shared.service';
import { Pet } from '../shared/Pet';

@Component({
  selector: 'app-pet',
  templateUrl: './pet.component.html',
  styleUrls: ['./pet.component.css']
})
export class PetComponent implements OnInit {

  constructor(private sharedService: SharedService, private renderer: Renderer2) { }

  pets: Pet[];
  selectedPet: Pet;

  ngOnInit(): void {
    this.getPets();
  }

  getPets(): void {
    this.sharedService.getPetList()
    .subscribe(pets => this.pets = pets);
  }

  onSelect(pet: Pet): void {
    this.selectedPet = pet;
    this.renderer.selectRootElement('.pet-details').scrollIntoView();
  }
}
