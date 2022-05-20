import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { EmployeesService } from '../api/employees.service';
import { Employee } from '../model/employee';
import { NewEmployee } from '../model/newEmployee';

@Component({
  selector: 'app-detail-employee',
  templateUrl: './detail-employee.component.html',
  styleUrls: ['./detail-employee.component.css']
})
export class DetailEmployeeComponent implements OnInit {
  employee$: Observable<Employee> | undefined;

  constructor(
    private employeeService: EmployeesService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.getEmployee()
  }

  getEmployee(): void {
    const id = this.route.snapshot.paramMap.get('id')!;
    this.employee$ = this.employeeService.getEmployeeById(id)
  }

  updateEmployee(employee: Employee, name: string, attr: string): void {
    var newemployee: NewEmployee = {
      name: name,
      attr: attr
    }
    this.employeeService.updateEmployee(employee.id, newemployee).subscribe(() => this.router.navigateByUrl('/'))
  }

  deleteEmployee(employee: Employee): void {
    this.employeeService.deleteEmployee(employee.id).subscribe(() => this.router.navigateByUrl('/'))
  }

}
