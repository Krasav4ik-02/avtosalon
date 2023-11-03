import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'site';


  async sendRequest() {
    let res = await fetch('https://localhost:8000').then((res) => res.json())
    console.log(res)
  }


}
