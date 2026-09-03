export const metresToFeet=(value:number)=>value*3.28084;
export const metresPerSecondToKnots=(value:number)=>value*1.94384;
export const metresPerSecondToFeetPerMinute=(value:number)=>value*196.8504;
export const formatNumber=(value:number|null,unit:string,digits=0)=>value===null?'--':`${value.toLocaleString('en-US',{maximumFractionDigits:digits})} ${unit}`;
