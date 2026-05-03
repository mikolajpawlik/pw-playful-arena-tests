import { test, expect } from '@playwright/test';

test.describe('Smoke tests', () => {
  test('app loads successfully', async ({ page }) => {
    await page.goto('/');
    await expect(page).not.toHaveTitle('');
    await expect(page.locator('body')).toBeVisible();
  });

  test('PWA manifest is present', async ({ page }) => {
    await page.goto('/');
    const manifestLink = page.locator('link[rel="manifest"]');
    await expect(manifestLink).toHaveCount(1);
  });
});
