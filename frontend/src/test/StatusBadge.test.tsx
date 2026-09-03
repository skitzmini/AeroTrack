import {render,screen} from '@testing-library/react';import {describe,expect,it} from 'vitest';import {StatusBadge} from '../components/StatusBadge';
describe('StatusBadge',()=>{it('shows airborne state',()=>{render(<StatusBadge onGround={false}/>);expect(screen.getByText('EM VOO')).toBeInTheDocument()})});
