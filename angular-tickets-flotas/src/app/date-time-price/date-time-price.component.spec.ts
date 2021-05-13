import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DateTimePriceComponent } from './date-time-price.component';

describe('DateTimePriceComponent', () => {
  let component: DateTimePriceComponent;
  let fixture: ComponentFixture<DateTimePriceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DateTimePriceComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DateTimePriceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
