# src/cyberinsight/services/qr_decoder_service.py
import io
import base64
import re
import logging
from typing import Optional, Dict, Any
from PIL import Image
from pyzbar import pyzbar
import cv2
import numpy as np

logger = logging.getLogger(__name__)

class QRDecoderService:
    """Service for decoding QR codes from images"""
    
    @staticmethod
    def decode_image(image_data: bytes) -> Optional[str]:
        """Decode QR code from image bytes using multiple methods"""
        try:
            # Validate input
            if not image_data or len(image_data) == 0:
                logger.warning("Empty image data provided")
                return None
            
            # Method 1: Using PIL + pyzbar
            try:
                image = Image.open(io.BytesIO(image_data))
                decoded_objects = pyzbar.decode(image)
                
                for obj in decoded_objects:
                    if obj.type == 'QRCODE':
                        return obj.data.decode('utf-8')
            except Exception as e:
                logger.debug(f"PIL decoding method failed: {str(e)}")
            
            # Method 2: Using OpenCV
            try:
                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if img is not None:
                    # Convert to grayscale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    
                    # Try different preprocessing methods
                    for method in [
                        lambda x: x,  # Original
                        lambda x: cv2.threshold(x, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1],  # Otsu
                        lambda x: cv2.adaptiveThreshold(x, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2),  # Adaptive
                    ]:
                        try:
                            processed = method(gray)
                            decoded = pyzbar.decode(processed)
                            for obj in decoded:
                                if obj.type == 'QRCODE':
                                    return obj.data.decode('utf-8')
                        except Exception:
                            continue
                    
                    # Try edge detection
                    try:
                        edges = cv2.Canny(gray, 50, 150)
                        decoded = pyzbar.decode(edges)
                        for obj in decoded:
                            if obj.type == 'QRCODE':
                                return obj.data.decode('utf-8')
                    except Exception:
                        pass
            except Exception as e:
                logger.debug(f"OpenCV decoding method failed: {str(e)}")
            
            return None
            
        except Exception as e:
            logger.error(f"Error decoding image: {str(e)}")
            return None
    
    @staticmethod
    def preprocess_image(image_data: bytes) -> bytes:
        """Preprocess image to improve QR code detection"""
        try:
            if not image_data:
                return image_data
                
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Enhance contrast
            try:
                from PIL import ImageEnhance
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(1.5)
            except Exception:
                pass
            
            # Resize if too large
            max_size = 1200
            if image.width > max_size or image.height > max_size:
                ratio = min(max_size / image.width, max_size / image.height)
                new_size = (int(image.width * ratio), int(image.height * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            return img_byte_arr.getvalue()
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {str(e)}")
            return image_data
    
    @staticmethod
    def is_valid_url(text: str) -> bool:
        """Check if text is a valid URL"""
        if not text:
            return False
        
        text = text.strip()
        
        # Check if it's a valid URL
        url_pattern = r'^https?://[^\s]+$'
        if re.match(url_pattern, text):
            return True
        
        # Check if it looks like a domain (e.g., example.com)
        domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
        if re.match(domain_pattern, text):
            return True
        
        # Check if it contains a URL
        url_in_text = r'https?://[^\s]+'
        if re.search(url_in_text, text):
            return True
        
        return False
    
    @staticmethod
    def extract_url(text: str) -> Dict[str, Any]:
        """Extract and validate URL from decoded text"""
        if not text:
            return {
                "url": None,
                "is_url": False,
                "message": "No content found in QR code"
            }
        
        text = text.strip()
        
        # Try to extract URL if it contains one
        url_pattern = r'https?://[^\s]+'
        urls = re.findall(url_pattern, text)
        
        if urls:
            return {
                "url": urls[0],
                "is_url": True,
                "message": "URL extracted successfully"
            }
        elif text.startswith('http://') or text.startswith('https://'):
            return {
                "url": text,
                "is_url": True,
                "message": "URL extracted successfully"
            }
        elif '.' in text and not text.startswith('http'):
            # Try to construct URL
            try:
                url_with_protocol = f"https://{text}"
                # Validate it's a proper domain
                domain_pattern = r'^https://[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
                if re.match(domain_pattern, url_with_protocol):
                    return {
                        "url": url_with_protocol,
                        "is_url": True,
                        "message": "URL constructed from domain"
                    }
            except:
                pass
            
            return {
                "url": text,
                "is_url": False,
                "message": "Text appears to be a domain but could not be validated as a URL"
            }
        else:
            return {
                "url": text,
                "is_url": False,
                "message": "QR code does not contain a valid URL"
            }
    
    @staticmethod
    def decode_from_base64(base64_data: str) -> Optional[Dict[str, Any]]:
        """Decode QR code from base64 encoded image"""
        try:
            if not base64_data:
                return {
                    "success": False,
                    "error": "No base64 data provided"
                }
            
            if ',' in base64_data:
                # Handle data URL format
                base64_data = base64_data.split(',')[1]
            
            try:
                image_bytes = base64.b64decode(base64_data)
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Invalid base64 data: {str(e)}"
                }
            
            return QRDecoderService.decode_from_bytes(image_bytes)
            
        except Exception as e:
            logger.error(f"Error decoding from base64: {str(e)}")
            return {
                "success": False,
                "error": f"Error processing base64 data: {str(e)}"
            }
    
    @staticmethod
    def decode_from_bytes(image_bytes: bytes) -> Optional[Dict[str, Any]]:
        """Decode QR code from bytes"""
        try:
            if not image_bytes:
                return {
                    "success": False,
                    "error": "No image data provided"
                }
            
            # First attempt with original image
            decoded_text = QRDecoderService.decode_image(image_bytes)
            
            # If failed, try with preprocessed image
            if not decoded_text:
                logger.info("Original image decoding failed, trying with preprocessing")
                preprocessed = QRDecoderService.preprocess_image(image_bytes)
                decoded_text = QRDecoderService.decode_image(preprocessed)
            
            if decoded_text:
                # Extract and validate URL
                url_info = QRDecoderService.extract_url(decoded_text)
                
                return {
                    "success": True,
                    "data": decoded_text,
                    "url": url_info["url"],
                    "is_url": url_info["is_url"],
                    "message": url_info["message"]
                }
            else:
                return {
                    "success": False,
                    "error": "No QR code found in the image",
                    "message": "Could not detect a QR code in the uploaded image"
                }
                
        except Exception as e:
            logger.error(f"Error decoding from bytes: {str(e)}")
            return {
                "success": False,
                "error": f"Error processing image: {str(e)}"
            }