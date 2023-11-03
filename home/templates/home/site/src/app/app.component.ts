import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'site';


  async sendRequest() {
    let res = await fetch('http://localhost:8000')
    let data = res
    console.log(data)
  }


}
