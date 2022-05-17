import { Component, OnInit } from '@angular/core';
import { EmployeesService } from '../api/employees.service';
import { NewEmployee } from '../model/newEmployee';

@Component({
  selector: 'app-create-employee',
  templateUrl: './create-employee.component.html',
  styleUrls: ['./create-employee.component.css']
})
export class CreateEmployeeComponent implements OnInit {

  constructor(private employeeServvice: EmployeesService) { }

  ngOnInit(): void {
  }

  createEmployee(name: string, attr: string): void {
    var newemployee: NewEmployee = {
      name: name,
      attr: attr
    };
    this.employeeServvice.createEmployee(newemployee).subscribe()
  }

}
