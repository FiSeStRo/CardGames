import { BASE_URL } from "./api.types";
import { Card } from "./utils.types";
import axios from 'axios';

const api = axios.create({
  baseURL: BASE_URL,
  headers: { 'Content-Type': 'application/json' }
});

export async function postHandResults(cards:Card[]){
    try {
      const test = JSON.stringify({ cards })
      const requestData = JSON.parse(test);
      console.log(requestData)
        const response = await api.post('/hand-results', {
          params: {data:requestData}
        });
        console.log("response",response.data);
        return response.data
      } catch (error) {
        console.log(error);
      }
}