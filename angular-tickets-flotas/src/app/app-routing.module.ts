import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BusComponent } from './bus/bus.component';
import { DateTimePriceComponent } from './date-time-price/date-time-price.component';
import { RoutesComponent } from './routes/routes.component';

const routes: Routes = [
  {path: 'routes', component:RoutesComponent},
  {path: 'date-time-price', component:DateTimePriceComponent},
  {path: 'bus', component:BusComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
