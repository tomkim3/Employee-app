import { Component} from '@angular/core';
import { ICellRendererAngularComp } from 'ag-grid-angular';

@Component({
  selector: 'app-detail-button',
  template: '<button mat-raised-button (click)="onClick($event)">{{label}}</button>'
})
export class DetailButtonComponent implements ICellRendererAngularComp {
  private params: any;
  label: string;

  agInit(params: any): void {
    this.params = params;
    this.label = this.params.label || null;
  }

  onClick($event: any) {
    if (this.params.onClick instanceof Function) {
      // put anything into params u want pass into parents component
      const params = {
        event: $event,
        rowData: this.params.node.data
        // ...something
      }
      this.params.onClick(params);

    }
  }

  ngOnDestroy() {
    // no need to remove the button click handler 
    // https://stackoverflow.com/questions/49083993/does-angular-automatically-remove-template-event-listeners
  }

  refresh(params?: any): boolean {
    return true;
  }
}
