import { keepPreviousData, useQuery } from '@tanstack/react-query';
import { api } from '../services/api';
import type { Bounds } from '../types/aviation';
const interval=Math.max(5000,Number(import.meta.env.VITE_VOO_REFRESH_INTERVAL ?? 10000));
export function useFlights(bounds?:Bounds){return useQuery({queryKey:['aircraft',bounds],queryFn:({signal})=>api.aircraft(bounds,signal),placeholderData:keepPreviousData,refetchInterval:interval,staleTime:interval/2,retry:2});}
export function useAircraft(icao24:string|null){return useQuery({queryKey:['aircraft',icao24],queryFn:()=>api.aircraftById(icao24!),enabled:Boolean(icao24)});}
