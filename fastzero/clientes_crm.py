from httpx import get


leads = get(
   "https://habitnet.nocrm.io/api/v2/leads",
   headers={"X-USER-TOKEN": "Mblvwkxo9YL-wavpEJ9CGA"}
   ).json()


