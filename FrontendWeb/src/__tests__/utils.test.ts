import { describe, expect, test } from 'vitest'
import { getRandomInt } from '../utils';

describe('utils', () => {
  test('getRandomInt', () => {
    expect(getRandomInt(3)).toBeLessThanOrEqual(3);
  })
});