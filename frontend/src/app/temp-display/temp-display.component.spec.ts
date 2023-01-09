import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TempDisplayComponent } from './temp-display.component';

describe('TempDisplayComponent', () => {
  let component: TempDisplayComponent;
  let fixture: ComponentFixture<TempDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TempDisplayComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TempDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
