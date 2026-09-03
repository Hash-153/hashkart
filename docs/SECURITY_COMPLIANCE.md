# NovaMart Security, Cryptography & Regulatory Compliance Policy

NovaMart is built from the ground up to comply with Indian data protection laws (Digital Personal Data Protection Act - DPDP 2023), Reserve Bank of India (RBI) Payment Aggregator & Card Tokenization guidelines, and Goods & Services Tax (GST) e-invoicing mandates.

---

## 1. Cryptographic Safeguards & Data At Rest / In Transit

- **TLS 1.3 Transport Security**: All external and internal pod-to-pod communications enforce TLS 1.3 with Perfect Forward Secrecy (PFS) using ECDHE cipher suites.
- **AES-256 Storage Encryption**: Database volumes (Aurora EBS), Redis cache instances, and S3 media buckets are encrypted at rest with AWS KMS customer-managed keys (CMK) rotated annually.
- **Passlib Argon2 / Bcrypt Password Hashing**: Customer and seller passwords are never stored in plaintext and are salted using standard bcrypt/Argon2 hashing with work factors >= 12.
- **JWT Signing & Rotation**: Short-lived (15-minute) asymmetric Ed25519/RS256 access tokens paired with 14-day cryptographically random refresh tokens stored in HTTP-only, secure, SameSite cookies.

---

## 2. Reserve Bank of India (RBI) Payment Compliance

1. **Card-on-File Tokenization (CoFT)**: NovaMart never stores raw 16-digit Primary Account Numbers (PAN) or Card Verification Values (CVV). All saved cards use RBI-mandated network tokens issued directly by Visa, Mastercard, or RuPay.
2. **Two-Factor Authentication (2FA)**: All payment authorizations enforce mandatory OTP / 3DS2 biometric challenges through licensed RBI payment gateways (Razorpay, Cashfree, PayU).
3. **Escrow Account Segregation**: Merchant funds are held in scheduled commercial bank nodal escrow accounts separate from NovaMart corporate operating funds.

---

## 3. GST & Tax Deductions (TCS / TDS)

Under Section 52 of the Central Goods and Services Tax (CGST) Act, 2017 and Section 194-O of the Income Tax Act, 1961:
- **1% TCS Withholding**: NovaMart automatically deducts 1% TCS on the net value of taxable supplies made through the platform.
- **1% / 0.1% TDS Withholding**: Deducted on gross sale amounts and credited directly to the seller's PAN.
- **GSTR-8 Monthly Filing**: Automated reports are generated at the close of every calendar month summarizing total supplies and tax withheld.

---

## 4. Webhook Security & Tamper Proofing

Outbound webhooks sent to seller systems include an HMAC-SHA256 signature in the `X-NovaMart-Signature` header:
$$\text{Signature} = \text{HMAC-SHA256}(\text{SecretKey}, \text{Timestamp} + "." + \text{PayloadBody})$$

Receiving endpoints verify this signature and reject timestamps older than 300 seconds to eliminate replay attacks.
