export * from './default.service';
import { DefaultService } from './default.service';
export * from './employees.service';
import { EmployeesService } from './employees.service';
export const APIS = [DefaultService, EmployeesService];
