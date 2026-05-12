# Component Evidence Rules

## Hard Rules

1. Vendor part number is not footprint proof.
2. Supplier CAD model is not automatically trusted.
3. Footprint and package claims require source-backed evidence.
4. ESP32 modules require antenna keepout and land-pattern proof.
5. USB-C and barrel-jack connectors require orientation and mechanical proof.
6. PMOS, regulator, ESD, and TVS parts require pin-mapping proof.
7. If the raw source is license-sensitive, store only normalized evidence here and quarantine the raw file.

## Evidence Priority

1. official datasheet
2. official package drawing
3. official land-pattern recommendation
4. official mechanical drawing
5. trusted verification record already stored in the repo

## Not Enough

- package name similarity
- vendor search results
- distributor category pages
- CAD model availability alone
- another project using the same footprint name
