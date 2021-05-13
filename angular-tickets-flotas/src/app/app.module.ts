import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DescripcionComponent } from './descripcion/descripcion.component';
import { RoutesComponent } from './routes/routes.component';
import { NavComponent } from './nav/nav.component';
import { DateTimePriceComponent } from './date-time-price/date-time-price.component';
import { BusComponent } from './bus/bus.component';

@NgModule({
  declarations: [
    AppComponent,
    DescripcionComponent,
    RoutesComponent,
    NavComponent,
    DateTimePriceComponent,
    BusComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
