import { useQuery } from '@tanstack/react-query'; import { api } from '../services/api';
export const useFlightHistory=()=>useQuery({queryKey:['history'],queryFn:api.history});
export const useFlightHistoryItem=(id:string)=>useQuery({queryKey:['history',id],queryFn:()=>api.historyItem(id)});
export const useFlightPositions=(id:string)=>useQuery({queryKey:['history',id,'positions'],queryFn:()=>api.positions(id)});
