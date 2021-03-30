import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SharedService } from '../shared.service';
import { Donation } from '../shared/Donation';
import { formatDate } from "@angular/common";

@Component({
  selector: 'app-donation',
  templateUrl: './donation.component.html',
  styleUrls: ['./donation.component.css']
})
export class DonationComponent implements OnInit {

  @ViewChild('fform') donationFormDirective;

  donationForm: FormGroup;
  donation: Donation;
  donations: Donation[];

  //slider configuration
  max = 1000;
  min = 50;
  step = 50;
  thumbLabel = true;

  constructor(private fb: FormBuilder, private shared: SharedService) {
    this.createForm();
  }

  ngOnInit(): void {
    this.getDonations();
  }

  createForm() {
    this.donationForm = this.fb.group({
      amount: [0, Validators.required],
      message: ['', Validators.required],
      email: ['', Validators.required],
      contact_name: ['', Validators.required],
    });
  }

  onSubmit() {
    this.donation = this.donationForm.value;
    this.shared.addDonation(this.donation).subscribe(res => console.log(res.toString()));

    this.donationForm.reset({
      amount: 0,
      message: '',
      email: '',
      contact_name: '',
    });
    this.donationFormDirective.resetForm();

    this.getDonations();
  }

  getDonations() {
    this.shared.getDonationList().subscribe(donations => {
      donations.map(donation => donation.date = formatDate(donation.date, "dd/MM/yyyy", "en-US"));
      this.donations = donations;
    });
  }
}
