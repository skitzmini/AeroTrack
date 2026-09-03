import type { AircraftResponse, Airport, Bounds, FlightHistory, FlightPosition } from '../types/aviation';
const BASE=(import.meta.env.VITE_API_URL ?? 'http://localhost:8000').replace(/\/$/,'');
async function request<T>(path:string, signal?:AbortSignal):Promise<T>{const response=await fetch(`${BASE}${path}`,{signal});if(!response.ok){const body=await response.json().catch(()=>({detail:'API temporarily unavailable'})) as {detail?:string};throw new Error(body.detail ?? 'API temporarily unavailable');}return response.json() as Promise<T>}
export const api={
 aircraft:(bounds?:Bounds,signal?:AbortSignal)=>request<AircraftResponse>(`/api/aircraft${bounds?`?${new URLSearchParams(Object.entries(bounds).map(([k,v])=>[k,String(v)]))}`:''}`,signal),
 aircraftById:(id:string)=>request<AircraftResponse>(`/api/aircraft/${encodeURIComponent(id)}`),
 searchFlights:(q:string)=>request<AircraftResponse>(`/api/flights/search?q=${encodeURIComponent(q)}`),
 airports:(q:string)=>request<Airport[]>(`/api/airports/search?q=${encodeURIComponent(q)}`),
 history:()=>request<FlightHistory[]>('/api/history'),
 historyItem:(id:string)=>request<FlightHistory>(`/api/history/${id}`),
 positions:(id:string)=>request<FlightPosition[]>(`/api/history/${id}/positions`)
};
