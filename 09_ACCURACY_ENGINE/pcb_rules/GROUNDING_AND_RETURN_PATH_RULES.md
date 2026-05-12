# Grounding And Return Path Rules

## Canonical Status

This file is the canonical rule surface for GND continuity and return-path
review.

## Mandatory Rules

- Review GND return continuity for every critical route cluster.
- Avoid routing that splits the local reference plane under USB, clock, RF, or switching-sensitive nets.
- Keep connector protection, USB return paths, and regulator returns compact and direct.
- Do not treat “a ground pour exists” as proof that the return path is good.
- Review whether stitching is needed near connector shields, ESD returns, regulator grounds, and board-edge current returns.

## Blocking Conditions

- a route obviously cuts the local return path
- a keepout or slot forces a critical route to cross a reference break
- switching or USB return current must take a long detour
- GND stitching is missing where the design intent depends on it

## Source Registry References

- `url_000005` - Nexperia EMC / switching-behavior app note
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
