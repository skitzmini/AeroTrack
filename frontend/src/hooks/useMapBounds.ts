import { useCallback, useState } from 'react'; import type { Bounds } from '../types/aviation';
const initial:Bounds={lamin:-60,lomin:-120,lamax:70,lomax:60};
const normalize=(value:number,min:number,max:number)=>Math.round(Math.max(min,Math.min(max,value))*100)/100;
export function useMapBounds(){const [bounds,setBounds]=useState<Bounds>(initial);const update=useCallback((next:Bounds)=>setBounds(current=>{const stable={lamin:normalize(next.lamin,-90,90),lomin:normalize(next.lomin,-180,180),lamax:normalize(next.lamax,-90,90),lomax:normalize(next.lomax,-180,180)};return Object.keys(stable).every(key=>stable[key as keyof Bounds]===current[key as keyof Bounds])?current:stable}),[]);return {bounds,update};}
