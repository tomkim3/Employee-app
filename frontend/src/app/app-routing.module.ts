import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ListEmployeeComponent } from './list-employee/list-employee.component';
import { CreateEmployeeComponent } from './create-employee/create-employee.component';
import { DetailEmployeeComponent } from './detail-employee/detail-employee.component';

const routes: Routes = [
  { path: 'employees', component: ListEmployeeComponent },
  { path: 'create-employee', component: CreateEmployeeComponent },
  { path: '', redirectTo: '/employees', pathMatch: 'full' },
  { path: 'detail/:id', component: DetailEmployeeComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
