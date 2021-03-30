import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';
import { Leader } from '../shared/Leader';

@Component({
  selector: 'app-aboutus',
  templateUrl: './aboutus.component.html',
  styleUrls: ['./aboutus.component.css']
})
export class AboutusComponent implements OnInit {

  leaders: Leader[];
  
  constructor(private shared: SharedService) { }

  ngOnInit(): void {
    this.getLeadersList()
  }

  getLeadersList() {
    this.shared.getLeadersList().subscribe(leaders => this.leaders = leaders);
  }
}
