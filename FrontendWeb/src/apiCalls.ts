import { BASE_URL } from "./api.types";
import { Card } from "./utils.types";
import axios from 'axios';

const api = axios.create({
  baseURL: BASE_URL,
  headers: { 'Content-Type': 'application/json' }
});

export async function getCardResults(cards:Card[]){
    try {
        const response = await api.get('/result', {
          params: { cards }
        });
        console.log("response",response.data);
        return response.data
      } catch (error) {
        console.log("error", error);
      }
}