import { Component, Input, OnInit } from '@angular/core';
import { Pet } from '../shared/Pet';

@Component({
  selector: 'app-petdetails',
  templateUrl: './petdetails.component.html',
  styleUrls: ['./petdetails.component.css']
})
export class PetdetailsComponent implements OnInit {

  @Input()
  pet: Pet;

  constructor() { }

  ngOnInit(): void {
  }

}
