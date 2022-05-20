import { Component, OnInit } from '@angular/core';
import { Employee } from '../model/employee';
import { EmployeesService } from '../api/employees.service';
import { Observable } from 'rxjs';
import { ColDef } from 'ag-grid-community';
import { Router } from '@angular/router';
import { DetailButtonComponent } from '../detail-button/detail-button.component';

@Component({
  selector: 'app-list-employee',
  templateUrl: './list-employee.component.html',
  styleUrls: ['./list-employee.component.css']
})
export class ListEmployeeComponent implements OnInit {
  employees$: Observable<Employee[]>;

  frameworkComponents: any;

  columnDefs: ColDef[] = [
    { field: 'name' },
    { field: 'attr' },
    {
      field: 'Detail',
      cellRenderer: 'detailbuttonRenderer',
      cellRendererParams: {
        onClick: this.btnClick.bind(this),
        label: 'Detail'
      }
    }
  ];

  constructor(
    private employeeService: EmployeesService,
    private router: Router
  ) {
    this.frameworkComponents = {
      detailbuttonRenderer: DetailButtonComponent
    }
  }

  ngOnInit(): void {
    this.employees$ = this.employeeService.listEmployees()
  }

  btnClick(e: any): void {
    this.router.navigateByUrl('/detail/'+e.rowData.id)
  }

}
