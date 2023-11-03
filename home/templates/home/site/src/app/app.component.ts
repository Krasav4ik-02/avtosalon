import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'site';


  async sendRequest() {
    let res = await fetch('http://127.0.0.1:8000/home/site/src/index.html').then((res) => res.json())
    console.log(res.message)
  }


}
