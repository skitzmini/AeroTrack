import {describe,expect,it} from 'vitest';import {metresPerSecondToKnots,metresToFeet} from '../utils/units';
describe('aviation unit conversions',()=>{it('converts metres to feet',()=>expect(metresToFeet(1000)).toBeCloseTo(3280.84));it('converts m/s to knots',()=>expect(metresPerSecondToKnots(100)).toBeCloseTo(194.384))});
